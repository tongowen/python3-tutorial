def main():
    fish = 1 # 假设鱼的总数
    while True:
        total = fish
        enough = True
        
        total, enough = fish, True # 

        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = ((total - 1)  //  5) * 4
            else:
                enough = False
                break

        if enough:
            print(f'总共有{fish}条鱼')
            break # 不要break则有无限多个结果

        fish += 1


if __name__ == '__main__':
    main()
