setwd('~/Documents/VscodeProjects/tx/real-world experiment/moduleGraph')
library(simule)
library(rjson)
library(philentropy)
library(parallel)

graphics.off()
par(ask = F)
par(mfrow = c(1, 1))

### 导入数据，数据的格式为t*p*p，其中t是训练数据集的数量，p是特征数量

t = length(data) # 数据集数量
p = row_num = length(data[[1]]) # 特征数量
print(t)
print(p)

# 规范数据格式，方便计算
input_matrixs = list()
for (i in 1:t) {
  t = matrix(c(1:p * p), nrow = p, ncol = p)
  for (j in 1:p) {
    for (k in 1:p) {
      t[j, k] = data[[i]][[j]][[k]]
    }
  }
  input_matrixs[[i]] = t
}
# epsilon和lambda是simule算法的参数
# 在没有true label的情况下，没法通过某个衡量指标判断参数是否合适，以下参数并不一定合适
# for (epsilon in c(0.1, 0.2, 0.3, 0.4)) {
for (epsilon in c(0.00001, 0.0001, 0.001, 0.01, 0.1, 1)) {
  print("=====================")
  for (lambda in c(0.00001, 0.0001, 0.001, 0.01, 0.1, 1)) {
  # for (lambda in c(0.06, 0.07, 0.08, 0.09, 0.1)) {
    # 输出配置
    cat("epsilon:", epsilon, "lambda", lambda, "\n")
    
    result = simule(input_matrixs, lambda, epsilon, covType = "cov", TRUE) # 训练
    # result数据包含两部分内容
    # print(result[['share']])
    # print(result[['Graphs']])
    # 输出share的非零个数
    share = result[["share"]]
    cat("The number of nonzero entries:", sum(share!=0), "\n")
    
    # 保存数据
    # filename = paste("./mat_cov/share/graph_epsilon", epsilon, "lambda", lambda, ".json", sep="")
    # filename = paste("./mat_cov/share/graph_v2_epsilon", epsilon, "lambda", lambda, ".json", sep="")
    # cat(toJSON(result), file = filename)
   }
  
}
