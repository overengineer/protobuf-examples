import sys
import proto.account_pb2

def account():
    return proto.account_pb2.Account(
        id=42,
        name='Linux Torvalds',
        is_verified=True,
        follow_ids=[0, 1],
    )


if __name__ == "__main__":
    fns = {
        'account': account
    }
    print(fns[sys.argv[1]]())