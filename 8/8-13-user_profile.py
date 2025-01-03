from dataclasses import field


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('fabrice', 'viteau', age=54, language='python')
print(user_profile)
