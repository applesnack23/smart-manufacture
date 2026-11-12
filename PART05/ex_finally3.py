def run(text):
    try:
        n = int(text)
        print("1 try 끝:", n)
    except ValueError:
        print("2 except: 숫자가 아님")
    else:
        print("3 else: 오류 없음")
    finally:
        print("4 finally: 언제나")

run("10")
print("---")
run("열")
