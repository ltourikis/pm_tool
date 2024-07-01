import random
import string


def generate_random_name():
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return random.choice(first_names) + ' ' + random.choice(last_names)


def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)
    return name + '@' + domain


def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(random.randint(8, 16)))


def generate_random_company_name():
    prefixes = ['Global', 'International', 'National', 'Innovative', 'Dynamic', 'Elite', 'United', 'Universal',
                'Global', 'Advanced']
    suffixes = ['Technologies', 'Solutions', 'Systems', 'Enterprises', 'Consulting', 'Services', 'Incorporated',
                'Group', 'Networks', 'Industries']
    return random.choice(prefixes) + ' ' + random.choice(suffixes)


def generate_random_address():
    street_names = ['Main St', 'Broadway', 'Park Ave', 'Elm St', 'Maple Ave', 'Cedar Ln', 'Pine St', 'Oak Dr',
                    'Sunset Blvd', 'Lakeview Dr']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
              'Dallas', 'San Jose']
    states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA']
    zip_code = ''.join(random.choice(string.digits) for _ in range(5))

    street_address = str(random.randint(1, 999)) + ' ' + random.choice(street_names)
    city = random.choice(cities)
    state = random.choice(states)

    return f"{street_address}, {city}, {state} {zip_code}"


def generate_random_sublist(input_list):
    if not input_list:
        return []

    # Generate a random number of elements to select, between 1 and the length of the list
    num_elements = random.randint(1, len(input_list))

    # Randomly select that number of elements from the input list
    random_sublist = random.sample(input_list, num_elements)

    return random_sublist


if __name__ == '__main__':
    # Generate and print random data
    print("Random Name:", generate_random_name())
    print("Random Email:", generate_random_email())
    print("Random Password:", generate_random_password())
    print("Random Company Name:", generate_random_company_name())
    print("Random Address:", generate_random_address())
