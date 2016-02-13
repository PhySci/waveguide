# -*- coding: utf-8 -*-
"""
Class descibes uniform anisotropic magnetic waveguide

Methods are intended for calculation of eigen spectra of spin waves

@author: SuperMan
"""

import math

class waveguideClass:

    M0 = 1  # magnetization (units?)    
    w = 1   # width (units?)
    L = 1   # thickness (units?)
    H = 1000 # external magnetic field (units)
    nMax = 5 # highest order of width modes
    qMax = 5 # highest order of thickness modes
       
    
    
    # constructor
    def __init__(self):
        pass

    #TODO: create lists of available wave vecors Kq and Kn, calculate then in _init_ method

    # calculate array of allowed width modes
    def calcKq(self):
        
        return 1
    
    # available wave vectors
    def Kq(self,q):
        return  4*math.pi/(q*self.L)

    # available wave vectorss
    def Kn(self,n):
        return  4*math.pi/(n*self.w)
        
    #TODO: create lists of values Dq and Dn
    def Dq(self,q):
        return 1
        
    def Dn(self,n):
        return 1 
    
    def C1(self,k,q):
        kq = self.Kq(self,q)
        return 2/(k^2+kq^2)*( k*math.cos(0.5*k*self.w)*math.sin(0.5*kq*self.w)-kq*math.sin(0.5*k*self.w)*math.cos(0.5*kq*self.w))
        
    
    def C2(self,k,q):
        kq = self.Kq(self,q)
        return 2/(k^2+kq^2)*( k*math.sin(0.5*k*self.w)*math.cos(0.5*kq*self.w)-kq*math.cos(0.5*k*self.w)*math.sin(0.5*kq*self.w))
        
    def Fzero(self,q):
        return 1
        
    def I1(self,k,q1,q2):
        return self.Fzero(q1)*self.Fzero(q2)*self.C2()
    
    def I2(self,k,q1,q2):
        pass
    
        
    

        
        
    
        
        