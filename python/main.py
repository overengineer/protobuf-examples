import sys
import proto.account_pb2
import proto.user_pb2
import proto.product_pb2
import proto.phone_book_pb2
import proto.login_pb2
import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.wrappers_pb2
import google.protobuf.json_format

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

def wrappers():
    return [
        google.protobuf.wrappers_pb2.BoolValue(value=True),
        google.protobuf.wrappers_pb2.BytesValue(value=b'lorem ipsum'),
        google.protobuf.wrappers_pb2.FloatValue(value=3.17),
    ]

def serialize():
    a = account()
    path = 'account.bin'
    print(a)
    with open(path, 'wb') as f:
        data = a.SerializeToString()
        f.write(data)

    with open(path, 'rb') as f:
        data = f.read()
        a = proto.account_pb2.Account().FromString(data)
    print(a)
    
def to_json(message):
    return google.protobuf.json_format.MessageToJson(
        message,
        indent=None,
        preserving_proto_field_name=True
    )

def from_json(json_str, msg_type):
    return google.protobuf.json_format.Parse(
        json_str,
        msg_type(),
        ignore_unknown_fields=True
    )

def json():
    a = account()
    json_str = to_json(a)
    print(json_str) 
    msg = from_json(json_str, proto.account_pb2.Account)   
    print(msg)

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
        'wrappers': wrappers,
        'serialize': serialize,
        'json': json,
    }
    print(fns[sys.argv[1]]())