import time


class PID:
    def __init__(self):
        self.Kp = 0
        self.Kd = 0
        self.Ki = 0
        self.currtime = time.time()
        self.prevtime = self.currtime

        self.prev_error = 0

        self.Cp = 0
        self.Ci = 0
        self.Cd = 0

    def SetKp(self,invar):
        self.Kp = invar

    def SetKi(self,invar):
        self.Ki = invar

    def SetKd(self,invar):
        self.Kd = invar

    def SetPrevError(self,preverror):
        self.prev_error = preverror

    def GenOut(self,error):
        '''implementation of PID control

        Args:
            error (float): error from current state to target state

        Returns:
            (float): Adjustment according to the PID output
        '''
        self.currtime = time.time()
        dt = self.currtime - self.prevtime
        de = error - self.prev_error

        self.Cp = self.Kp*error
        self.Ci += error*dt

        self.Cd = 0
        if dt > 0:
            self.Cd = de/dt

        self.prevtime = self.currtime
        self.prev_error = error

        return self.Cp + (self.Ki*self.Ci) + (self.Kd*self.Cd)