def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Adds a new contact to the contact dictionary.

    :param args: List of arguments containing the name and phone number.
    :param contacts: Dictionary of contacts.
    :return: Confirmation message.
    """
    if len(args) != 2:
        return "Error: Please provide a name and a phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Changes the phone number of an existing contact.

    :param args: List of arguments containing the name and new phone number.
    :param contacts: Dictionary of contacts.
    :return: Confirmation message or error if contact is not found.
    """
    if len(args) != 2:
        return "Error: Please provide a name and a new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Returns the phone number for the given contact name.

    :param args: List of arguments containing the contact name.
    :param contacts: Dictionary of contacts.
    :return: Phone number or error if contact is not found.
    """
    if len(args) != 1:
        return "Error: Please provide a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(contacts: dict[str, str]) -> str:
    """
    Returns all saved contacts with phone numbers.

    :param contacts: Dictionary of contacts.
    :return: String with all contacts and phone numbers.
    """
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."