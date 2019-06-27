import numpy as np


class Solution(object):
    def EM_algorithm(self, x, p_x, max_itr, mean, var) -> int:
        '''

        :param groupA:
        :param groupB:
        :param weighting:  initial weighting for two gaussian distribution
        :return:
        '''
        itrMean, itrVar = mean, var
        itr = 0
        ans_p_x = p_x
        while itr < max_itr:
            print('*' * 20)
            print('itre: {:<5}'.format(itr))
            for i in range(len(itrMean)):
                print("Group {:<5}: [{:<5}, {:<5}] {:<5}".format(i,itrMean[i],itrVar[i],ans_p_x[i]))
            prob = self.gaussian(x,itrMean,itrVar)
            # print(prob)
            # print(prob.shape)
            # / np.sum(prob, axis=0)
            prob_normalization = np.multiply(prob.T, ans_p_x).T
            # print(prob_normalization)
            prob_normalization = prob_normalization / np.sum(prob_normalization,axis=0)
            # print(prob_normalization)
            # print(prob_normalization.shape)


            # EM: update X and mean Variance
            for i in range(prob_normalization.shape[0]):
                # print(x)
                # print(prob_normalization[i])
                itrVar[i] = np.sum((np.power(x - itrMean[i],2) * prob_normalization[i]) / np.sum(prob_normalization[i]))
                itrMean[i] = np.sum((x*prob_normalization[i]) / np.sum(prob_normalization[i]))
                # print(itrX)
                # print(itrX)
                # itrMean[i], itrVar[i] = np.mean(itrX), np.var(itrX)
                # GMM
                ans_p_x[i] = np.sum(prob_normalization[i]) / len(prob_normalization[i])

            itr +=1
        return 0

    def gaussian(self, x, mean, var):
        if x is None:
            return -1
        ans = np.zeros((2,len(x)))
        for i in range(len(mean)):
            c = 1/np.sqrt(2*np.pi*var[i])
            b = (-1*np.power(x-mean[i],2)) / (2*var[i])
            ans[i] = c*np.exp(b)
        return ans
if __name__ == '__main__':
    method = Solution()
    max_itr = 10
    # example A:
    al = 0.5  # P(X=1) = al
    p_x = np.array([1 - al, al])
    mean = [158, 172]
    var = [7.35, 39.46]
    inputX = np.array([155, 157, 157, 159, 163,165, 167, 172, 180, 180])
    method.EM_algorithm(inputX, p_x, max_itr, mean, var)