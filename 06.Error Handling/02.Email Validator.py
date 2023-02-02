from custom_extensions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

info = input()
valid_domains = {'.com', '.bg', '.org', '.net'}

while info != 'End':
    email = info.split('@')
    if len(email) == 2:
        name, second_part = email[0], email[1]
    else:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    end_of_domain = f".{second_part.split('.')[-1]}"

    if end_of_domain not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")
    print('Email is valid')

    info = input()
