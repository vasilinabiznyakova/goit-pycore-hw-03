import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num):
    cleaned_num = re.sub(r"[^0-9+]", "", num)

    if cleaned_num.startswith("+380"):
        return cleaned_num
    elif cleaned_num.startswith("380"):
        return "+" + cleaned_num
    else:
        return "+38" + cleaned_num


def normalize_phone_with_re(num):
    cleaned_num = re.sub(r"[^0-9+]", "", num)

    if re.match(r"^\+380", cleaned_num):
        return cleaned_num
    elif re.match(r"^380", cleaned_num):
        return "+" + cleaned_num
    else:
        return "+38" + cleaned_num


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)

sanitized_numbers = [normalize_phone_with_re(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)

# expected result
# ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
