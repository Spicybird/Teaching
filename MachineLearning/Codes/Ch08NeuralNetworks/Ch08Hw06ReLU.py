# TODO: 1. 导入必须库 以及 定义必要的函数
# 导入数据集工具包
from sklearn import datasets
from sklearn.model_selection import train_test_split
# 导入MLP神经网络包
from sklearn.neural_network import MLPClassifier

# TODO: 2. 创建/导入数据
iris = datasets.load_iris()

# TODO: 3. 数据预处理，包括训练集、测试集划分，数据正则化，数据清洗等
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.1, random_state=10)

# TODO: 4. 构建模型，并进行模型训练（或称为拟合数据）
mlp_ReLU = MLPClassifier(solver='lbfgs', random_state=10, activation='relu',
                         hidden_layer_sizes=[32, 128, 128])
mlp_ReLU.fit(X_train, y_train)

# TODO: 5. 输出预测结果
score_train = mlp_ReLU.score(X_train, y_train)
score_test = mlp_ReLU.score(X_test, y_test)
print("训练集准确率: {0:.4f}, 测试集准确率: {1:.4f}.".format(score_train, score_test))
