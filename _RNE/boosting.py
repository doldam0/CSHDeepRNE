from xgboost import XGBClassifier, plot_importance
from matplotlib import pyplot
from csv_to_list import get_data


X, y = get_data('data_classify.csv', 1)

model = XGBClassifier()
model.fit(X, y)
plot_importance(model)
pyplot.show()