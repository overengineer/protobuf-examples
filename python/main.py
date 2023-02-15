import sys
import proto.account_pb2
import proto.user_pb2
import proto.product_pb2
import proto.phone_book_pb2
import proto.login_pb2
import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.field_mask_pb2

def account():
    return proto.account_pb2.Account(
        id=42,
        name='Linux Torvalds',
        is_verified=True,
        follow_ids=[0, 1],
    )

def user():
    u = proto.user_pb2.User()
    u.id = 42
    u.name = 'Linux Torvalds'
    u.follows.add(id=0, name='Linux Foundation')
    return u

def product():
    return proto.product_pb2.Product(
        id = 42,
        type = proto.product_pb2.Product.Type.PANTS,
    )

def phone_book():
    return proto.phone_book_pb2.PhoneBook(
        phones = {
            'Linus Torvalds': '1111111111',
            'Linux Foundation': '5555555555',            
        }
    )

def login():
    return proto.login_pb2.LoginResult(
        token = proto.login_pb2.Token()
    )

def duration():
    import datetime
    d = google.protobuf.duration_pb2.Duration()
    d.FromTimedelta(datetime.timedelta(seconds=300))
    return d

def timestamp():
    import datetime
    t = google.protobuf.timestamp_pb2.Timestamp()
    t.GetCurrentTime()
    return t

def field_mask():
    a = account()
    fm = google.protobuf.field_mask_pb2.FieldMask(
        paths = [
            'id',
            'is_verified',
        ]
    )
    iiv = proto.account_pb2.Account()
    fm.MergeMessage(a, iiv)
    return iiv


if __name__ == "__main__":
    fns = {
        'account': account,
        'user': user,
        'product': product,
        'phone_book': phone_book,
        'login': login,
        'duration': duration,
        'timestamp': timestamp,
        'field_mask': field_mask,
    }
    print(fns[sys.argv[1]]())