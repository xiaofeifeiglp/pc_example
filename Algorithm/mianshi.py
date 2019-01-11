class main(object):
    def fun1(self):
        result1 = [
            {
                "uid": 1,
                "name": "cao"
            },
            {
                "uid": 2,
                "name": "c"
            },
            {
                "uid": 4,
                "name": "ca"
            },
            {
                "uid": 3,
                "name": "o"
            }
        ]
        result2 = [
            {
                "uid": 1,
                "age": "cao"
            },
            {
                "uid": 2,
                "age": "c"
            },
            {
                "uid": 3,
                "age": "o"
            },
            {
                "uid": 4,
                "age": "ca"
            }
        ]

        for r1 in result1:
            for r2 in result2:
                if r1["uid"] == r2["uid"]:
                    r1["age"] = r2["age"]
        print(result1)

    def fun2(self):
        result1_dict = {
            1: {
                "uid": 1,
                "name": "cao"
            },
            2: {
                "uid": 2,
                "name": "c"
            },
            3: {
                "uid": 3,
                "name": "o"
            },
            4: {

                "uid": 4,
                "name": "ca"
            }
        }

        result2 = [
            {
                "uid": 1,
                "age": "cao"
            },
            {
                "uid": 2,
                "age": "c"
            },
            {
                "uid": 3,
                "age": "o"
            },
            {
                "uid": 4,
                "age": "ca"
            }
        ]
        l = []
        for r2 in result2:
            result1_dict[r2["uid"]]["age"] = r2["age"]

        for x in range(1, 5):
            l.append(result1_dict[x])
        print(l)

if __name__ == '__main__':
    test = main()
    test.fun1()
    test.fun2()
