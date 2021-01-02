import csv
import numpy as np



class data:
    def __init__(self,batch=60,total_data_number=300,training_percent=0.98,
            file_path="./train_data/",file_name="train_data.csv"):
        self.batch = batch
        self.total_data_number = total_data_number
        self.current = 0
        self.training_percent = training_percent
        self.file_path = file_path
        self.file_name = file_name
        self.data = self.get_data()

    def get_batch_train_data(self):

        # check whether out of range
        if(self.current+self.batch>self.total_data_number*self.training_percent):
            self.current = 0
        train_data = self.data[self.current:self.current+self.batch]
        # reset current
        self.current = self.current + self.batch
        return train_data

    def get_test_data(self):
        print(self.data.shape)
        test_data = self.data[int(self.total_data_number*self.training_percent):self.total_data_number]
        return test_data

    def get_data(self):
        data= []
        with open(self.file_path+self.file_name,'r') as my_file:
            csv_reader = csv.reader(my_file,delimiter=',')
            for i in csv_reader:
                for j in range(len(i)):
                    i[j]=float(i[j])
                data.append(i)
        # convert list to array
        data = np.asarray(data,float)
        # data normalization
        for i in range(data.shape[0]):
            for j in range(data.shape[1]-2):
                pass
                #data[i,j] = data[i,j]/max(data[:,j])
        return data
    """
    parameter: index is an array, 1 means selected, 0 doesn't. [1,0,0,0,1,1,0]    
    """
    def get_batch_train_data_with_specific_attributes(self, index):
        batch_data = self.get_batch_train_data()
        list_result = list()
        for i in range(batch_data.shape[0]):
            included_attribute = list()
            for j in range(len(index)):
                if(index[j]==1):
                    included_attribute.append(batch_data[i,j])
            list_result.append(included_attribute)
        # convet list to array
        array_result= np.asarray(list_result,float)
        return array_result


if __name__ == '__main__':
     data = data(batch=5)
     #train_data =data.get_batch_train_data()
     #index = np.random.randint(0,2,(14))
     #result = data.get_batch_train_data_with_specific_attributes(index)
     test_data = data.get_test_data()
     print(test_data)


# save normalized data
"""
with open("normalized.data",'w') as handler:
    csv_handler = csv.writer(handler,delimiter=',')
    for i in range(data.shape[0]):
        csv_handler.writerow(data[i,:])
"""




