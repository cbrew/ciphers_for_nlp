import numpy as np

class HMM:
    """
    Hidden Markov Model
    """
    def __init__(self,M,N,seed=42):

        self.rng = np.random.default_rng(seed=seed)
        self.N = N
        self.M = M
        A = np.random.random(size=(N,N))
        self.A = (A/A.sum(axis=0)).T
        B = np.random.random(size=(M,N))
        self.B = (B/B.sum(axis=0)).T
        self.pi = np.random.random(size=N)
        self.pi /= self.pi.sum()

    class LogProbs:
        def __init__(self,model):
            self.model = model

        def __enter__(self):
            self.model.pi = np.log(self.model.pi)
            self.model.A = np.log(self.model.A)
            self.model.B = np.log(self.model.B)

        def __exit__(self,exc_type, exc_value, traceback):
            self.model.pi = np.exp(self.model.pi)
            self.model.A = np.exp(self.model.A)
            self.model.B = np.exp(self.model.B)

    def generate(self,n, states = False):
        state = self.rng.choice(a=self.N,p=self.pi)
        for _ in range(n):
            yield self.rng.choice(a=self.M,p=self.B[state])
            state = self.rng.choice(a=self.N,p=self.A[state])

    def viterbi(self, seq):
        """
        Decode emission sequence using
        Viterbi algorithm.

        :param seq:
        :return:
        """
        with self.LogProbs(self):
            best_score = np.array(self.pi)
            backtrace = [list(range(self.N))]
            for item in seq:
                transition_probs = self.A
                emission_probs = self.B[:,item]
                routes =  transition_probs + emission_probs + best_score
                best_score = np.min(
                    routes,
                    axis=0)
                steps = np.argmax(routes,
                                  axis=0)
                backtrace.append(steps)
            return backtrace,best_score











if __name__ == "__main__":
    hmm = HMM(26,3)
    print(hmm.viterbi([0,1]))
