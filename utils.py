import re

def parse_lab_report_text(text: str):
    result = []
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith("Test Name") or "Interpretation" in line:
            continue  
          
        match1 = re.match(r"(.+?)\s+([\d.]+)\s+([a-zA-Z/%]+)?\s+\(?([\d.]+)-([\d.]+)\)?", line)
        if match1:
            test_name = match1.group(1).strip()
            test_value = float(match1.group(2))
            test_unit = match1.group(3) or ""
            ref_low = float(match1.group(4))
            ref_high = float(match1.group(5))
            out_of_range = not (ref_low <= test_value <= ref_high)

            result.append({
                "test_name": test_name,
                "test_value": str(test_value),
                "test_unit": test_unit,
                "bio_reference_range": f"{ref_low}-{ref_high}",
                "lab_test_out_of_range": out_of_range
            })
            continue

        match2 = re.match(r"(.+?)\s+(NEGATIVE|POSITIVE|NORMAL|ABNORMAL)", line, re.IGNORECASE)
        if match2:
            result.append({
                "test_name": match2.group(1).strip(),
                "test_value": match2.group(2).upper(),
                "test_unit": "",
                "bio_reference_range": "",
                "lab_test_out_of_range": False
            })
            continue


    return result
