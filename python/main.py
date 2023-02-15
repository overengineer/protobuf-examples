import sys
import proto.account_pb2
import proto.user_pb2
import proto.product_pb2

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



if __name__ == "__main__":
    fns = {
        'account': account,
        'user': user,
        'product': product,
    }
    print(fns[sys.argv[1]]())