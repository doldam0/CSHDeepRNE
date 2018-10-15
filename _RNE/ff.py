#######################
#    Park Geup Sick   #
#######################
# start from 2018-8-9 #
#       made by       #
#     Kim DongHyeon   #
#     Jang JinWoo     #
#       GODPARK       #
#######################

# Import package
from keras.layers import Dense
from keras.models import Sequential
from matplotlib import pyplot as plt
from csv_to_list import get_data


def run():
    # Data
    x_train, y_train, x_test, y_test = get_data('data_classify.csv', 0.8)

    # Design
    model = Sequential()
    num_of_hidden = 3
    hidden_layer = 8
    model.add(Dense(units=hidden_layer, input_dim=9, activation='relu'))
    for i in range(num_of_hidden):
        model.add(Dense(units=hidden_layer, activation='relu'))
    model.add(Dense(units=5, activation='softmax'))

    # Compile
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fitting
    this_epochs = 500
    this_batch_size = 25
    hist = model.fit(x_train, y_train, epochs=this_epochs, batch_size=this_batch_size)

    # Process
    print(' ## GOD PARK GEUP SICK ## ')
    print(hist.history['loss'])
    print(hist.history['acc'])

    # Evaluate
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=this_batch_size)
    print(' ## GOD PARK GEUP SICK IS BEING EVALUATED ## ')
    print('loss and metrics')
    print(loss_and_metrics)

    # Save
    print(' ## Now Saving... ## ')
    json_string = model.to_json()
    model.save('park_sick.h5')
    print(' ## ...Success! ## ')

    # Graph
    plt.title('Loss')
    plt.plot(hist.history['loss'])
    plt.show()

    plt.title('Accuracy')
    plt.plot(hist.history['acc'], c='y')
    plt.show()


if __name__ == "__main__":
    run()
