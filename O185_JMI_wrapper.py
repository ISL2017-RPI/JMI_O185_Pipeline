import sys
import JMI_O185
import numpy as np

def JMI(data_file = 'trainData.csv', target_file = 'trainargets.csv', hm_feat = 10):
    my_JMI = JMI_O185.initialize()
    feat = my_JMI.JMI_primitive_O185(data_file, target_file, hm_feat)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    hm_feat = 10
    selected_feature = np.array(JMI(data, target, hm_feat), dtype=np.int16)
    np.savetxt('Features_O185_JMI.csv', selected_feature, delimiter=',')
    print selected_feature
