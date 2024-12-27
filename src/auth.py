import bcrypt


def str2bytes(string: str) -> bytes:
    return string.encode(encoding="utf-8", errors="strict")


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(str2bytes(password), bcrypt.gensalt(14))


def password_match(password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(str2bytes(password), str2bytes(hashed_password))
    except:
        return False
