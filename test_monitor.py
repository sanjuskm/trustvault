import time
from trustvaultClient.trustvault_sdk import vault_it # from trustvault_sdk import vault_it

@vault_it
def add(a, b):
    time.sleep(0.1)
    return a + b

@vault_it(name="custom_mul")
def mul(a, b):
    time.sleep(0.05)
    return a * b

@vault_it
def errored():
    raise ValueError("Test error")

@vault_it
def outer(a, b):
    # Nested spans: calls to decorated functions inherit the trace
    result1 = add(a, b)
    result2 = mul(a, b)
    return result1 + result2

def main():
    print("add:", add(2, 3))
    try:
        errored()
    except Exception as e:
        print("Caught error:", e)
    print("mul:", mul(4, 5))
    print("outer:", outer(5, 6))

if __name__ == "__main__":
    main()