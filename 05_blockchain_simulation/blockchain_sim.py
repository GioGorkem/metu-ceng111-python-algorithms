# """
# TS<2077><12><01> ID:991-XBTC $$5000$$(VOID)
# TS<2077><12><02> ID:NET-001 $$100$$
# SYSTEM_LOG: DATA BREACH DETECTED AT NODE 4
# TS<2077><12><03> ID:110-ETH $$20$$(PEND)
# """

def fix_ledger(corrupted_logs):
    lines = corrupted_logs.split("\n")
    clear_lines = [clean_lines(line) for line in lines]
    control_breach = [line for line in lines if "BREACH" in line]
    if control_breach:
        clear_lines.insert(0, "STATUS: CRITICAL")
    else:
        clear_lines.insert(0, "STATUS: VERIFIED")
    exact_output = "\n".join(clear_lines)
    return exact_output
    
def clean_lines(line):
    #line: TS<2077><12><01> ID:991-XBTC $$5000$$(VOID)
    if not line:
        return line
    stripped_line = line.lstrip()
    indentet_part = line[:len(line)-len(stripped_line)]
    if not stripped_line:
        return line
    if stripped_line.startswith("TS"):
        non_organized_parts = stripped_line.split(" ")
        # non_organized_parts: ['TS<2077><12><01>', 'ID:991-XBTC', '$$5000$$(VOID)']
        organized_line_list = [organize_parts(part) for part in non_organized_parts]
        organized_line = " ".join(organized_line_list)
        return organized_line
    else:
        return line
def organize_parts(part):
    # non_organized_parts: ['TS<2077><12><01>', 'ID:991-XBTC', '$$5000$$(VOID)']
    # part: 'TS<2077><12><01>'
    if part.startswith("TS"):
        part = part.replace("TS", "").replace("<", "").replace(">", "")
        part_year, part_month, part_day = part[:4], part[4:6], part[6:]
        part_correct_date = f"{part_day}.{part_month}.{part_year}"
        return part_correct_date
    elif part.startswith("ID"):
        part_just_id = part.replace("ID:", "")
        if part_just_id[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            numbers_codes = part_just_id.split("-")

            return f"{numbers_codes[1]}-{numbers_codes[0][::-1]}"
        else:
            return part_just_id
    elif part.startswith("$$"):
        part_clear = part.replace("$$", "")
        if "(VOID)" in part_clear:
            return "CANCELLED"
        elif "(PEND)" in part_clear:
            return f"[!]{part_clear.replace("(PEND)", "")}"
        else:
            return part_clear
        
