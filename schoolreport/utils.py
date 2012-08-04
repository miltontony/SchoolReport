def phone_number_to_international(phone_number):
    if phone_number.startswith('27') and len(phone_number) == 11:
        return phone_number
    elif phone_number.startswith('0') and len(phone_number) == 10:
        return '27' + phone_number[1:]
    else:
        return 'invalid no'


def process_post_data_username(post):
    """
    converts username(phone number) to valid
    international phone number (27821234567)
    """
    if not post.get('username', None):
        return post

    post_data = post.copy()
    post_data['username'] = phone_number_to_international(post_data['username'])
    return post_data
