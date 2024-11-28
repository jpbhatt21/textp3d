
W = [0,0,0]
epochs =2

def predict(x):
    z = 0
    for i in range(3):
        z+=W[i]*x[i]
    a = (1 if z >= -1 else -1)
    return a

def fit( X, d):
    global W
    for _ in range(epochs):
        for i in range(len(d)):
            x = [1] + X[i]
            y = predict(x)
            e = d[i] - y
            z=[]
            for j in range(len(W)):
                z.append(W[j]+e*x[j])
            W = z

X = [
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]

d = [-1, 1, 1, 1]
fit(X, d)
print("Trained weights:", W)

for x in X:
    x = [1] + x
    print("Input: [",x[1],",",x[2],"] -> Predicted Output: ",predict(x))