
#LINK https://www.hackerrank.com/challenges/jim-and-the-orders/problem?isFullScreen=true

def jimOrders(orders):
    serve_time = [(order+time,i) for (i,(order,time)) in enumerate(orders,1)]
    serve_time = sorted(serve_time, key=(lambda orders: orders[0]))
    arr = [x for (y,x) in serve_time]
    return arr

if __name__ == '__main__':
    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(*result)
