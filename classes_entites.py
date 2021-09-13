#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:38:08 2021

@author: willy
"""

import time
import math
import numpy as np

# ----------------------------------------------------------------
#           definition of Smartgrid Class
# ----------------------------------------------------------------
class Smartgrid:
    
    def __init__(self, smartgrid_id, name):
        self.smartgrid_id = smartgrid_id
        self.name = name
        
    # ----------------- definition of setters -----------------
    def set_smartgrid_id(self, smartgrid_id):
        self.smartgrid_id = smartgrid_id
    
    def set_name(self, name):
        self.name = name
    
    # ----------------- definition of getters -----------------
    def get_smartgrid_id(self):
        return self.smartgrid_id
    
    def get_name(self):
        return self.name

# ----------------------------------------------------------------
#           definition of Agent Class
# ----------------------------------------------------------------
class Agent:
    
    def __init__(self, agent_id, smartgrid_id, name):
        self.agent_id = agent_id
        self.smartgrid_id = smartgrid_id
        self.name = name
        
    # ----------------- definition of setters -----------------
    def set_agent_id(self, agent_id):
        self.agent_id = agent_id
        
    def set_smartgrid_id(self, smartgrid_id):
        self.smartgrid_id = smartgrid_id
    
    def set_name(self, name):
        self.name = name
    
    # ----------------- definition of getters -----------------
    def get_agent_id(self, agent_id):
        return self.agent_id
        
    def get_smartgrid_id(self):
        return self.smartgrid_id
    
    def get_name(self):
        return self.name
    
# ----------------------------------------------------------------
#           definition of Period Class
# ----------------------------------------------------------------
class Period:
    
    def __init__(self, period_id, agent_id, Pi_t, Ci_t, Si_init_t,
                 Si_max, t, state_i, Si_t_minus, Si_t_plus, ppi_t,
                 gamma_i_t, q_t_minus, q_t_plus):
      self.period_id = period_id 
      self.agent_id = agent_id
      self.Pi_t = Pi_t
      self.Ci_t = Ci_t
      self.Si_init_t = Si_init_t
      self.Si_max = Si_max
      self.t = t 
      self.state_i = state_i
      self.Si_t_minus = Si_t_minus
      self.Si_t_plus = Si_t_plus
      self.ppi_t = ppi_t
      self.gamma_i_t = gamma_i_t
      self.q_t_minus = q_t_minus
      self.q_t_plus = q_t_plus
    
    # ----------------- definition of setters -----------------
    def set_period_id(self, period_id):
        self.period_id = period_id
    
    def set_agent_id(self, agent_id):
        self.agent_id = agent_id
        
    def set_Pi_t(self, Pi_t):
        self.Pi_t = Pi_t
        
    def set_Ci_t(self, Ci_t):
        self.Ci_t = Ci_t
        
    def set_Si_init_t(self, Si_init_t):
        self.Si_init_t = Si_init_t
        
    def set_Si_max(self, Si_max):
        self.Si_max = Si_max
    
    def set_Si_t_minus(self, Si_t_minus):
        self.Si_t_minus = Si_t_minus
        
    def set_Si_t_plus(self, Si_t_plus):
        self.Si_t_plus = Si_t_plus
    
    def set_ppi_t(self, ppi_t):
        self.ppi_t = ppi_t
        
    def set_gamma_i_t(self, gamma_i_t):
        self.gamma_i_t = gamma_i_t
        
    def set_q_t_minus(self, q_t_minus):
        self.q_t_minus = q_t_minus
        
    def set_q_t_plus(self, q_t_plus):
        self.q_t_plus = q_t_plus
    
    # ----------------- definition of getters -----------------
    def get_period_id(self):
        return self.period_id
    
    def get_agent_id(self):
        return self.agent_id
        
    def get_Pi_t(self):
        return self.Pi_t
        
    def get_Ci_t(self):
        return self.Ci_t
        
    def get_Si_init_t(self):
        return self.Si_init_t
        
    def get_Si_max(self):
        return self.Si_max
    
    def get_Si_t_minus(self):
        return self.Si_t_minus
        
    def get_Si_t_plus(self):
        return self.Si_t_plus
    
    def get_ppi_t(self):
        return self.ppi_t
        
    def get_gamma_i_t(self):
        return self.gamma_i_t
        
    def get_q_t_minus(self):
        return self.q_t_minus
        
    def get_q_t_plus(self):
        return self.q_t_plus
    
    

# ----------------------------------------------------------------
#           definition of LearningStep Class
# ----------------------------------------------------------------
class LearningStep:
    
    def __init__(self, learning_step_id, period_id, mode_i, k_step, 
                 prod_i, cons_i, Si, r_i, ben_i, cst_i, V_i, u_i, 
                 bg_i, prob_i_1, prob_i_2):
      self.learning_step_id = learning_step_id 
      self.period_id = period_id 
      self.mode_i = mode_i
      self.k_step = k_step
      self.prod_i = prod_i
      self.cons_i = cons_i
      self.Si = Si
      self.r_i = r_i
      self.ben_i = ben_i
      self.cst_i = cst_i
      self.V_i = V_i
      self.u_i = u_i
      self.bg_i = bg_i
      self.prob_i_1 = prob_i_1
      self.prob_i_2 = prob_i_2
      
    # ----------------- definition of setters -----------------
    def set_learning_step_id(self, learning_step_id):
        self.learning_step_id = learning_step_id
    
    def set_period_id(self, period_id):
        self.period_id = period_id
        
    def set_mode_i(self, mode_i):
        self.mode_i = mode_i
        
    def set_k_step(self, k_step):
        self.k_step = k_step
        
    def set_prod_i(self, prod_i):
        self.prod_i = prod_i
    
    def set_cons_i(self, cons_i):
        self.cons_i = cons_i
        
    def set_Si(self, Si):
        self.Si = Si
    
    def set_r_i(self, r_i):
        self.r_i = r_i
        
    def set_ben_i(self, ben_i):
        self.ben_i = ben_i
    
    def set_cst_i(self, cst_i):
        self.cst_i = cst_i
        
    def set_V_i(self, V_i):
        self.V_i = V_i
        
    def set_u_i(self, u_i):
        self.u_i = u_i
        
    def set_bg_i(self, bg_i):
        self.bg_i = bg_i
        
    def set_prob_i_1(self, prob_i_1):
        self.prob_i_1 = prob_i_1
        
    def set_prob_i_2(self, prob_i_2):
        self.prob_i_2 = prob_i_2
    
    # ----------------- definition of getters -----------------
    def get_learning_step_id(self):
        return self.learning_step_id
    
    def get_period_id(self):
        return self.period_id
        
    def get_mode_i(self):
        return self.mode_i
        
    def get_k_step(self):
        return self.k_step
        
    def get_prod_i(self):
        return self.prod_i
    
    def get_cons_i(self):
        return self.cons_i
        
    def get_Si(self):
        return self.Si
    
    def get_r_i(self):
        return self.r_i
        
    def get_ben_i(self):
        return self.ben_i
    
    def get_cst_i(self):
        return self.cst_i
        
    def get_V_i(self):
        return self.V_i
        
    def get_u_i(self):
        return self.u_i
        
    def get_bg_i(self):
        return self.bg_i
        
    def get_prob_i_1(self):
        return self.prob_i_1
        
    def get_prob_i_2(self):
        return self.prob_i_2

# ----------------------------------------------------------------
#           definition of Price Class
# ----------------------------------------------------------------
class Price:
    
    def __init__(self, price_id, period_id, b0_t, c0_t, 
                 pi_0_t_plus, pi_0_t_minus, Out_sg_t, In_sg_t):
      self.price_id = price_id 
      self.period_id = period_id 
      self.b0_t = b0_t
      self.c0_t = c0_t
      self.pi_0_t_plus = pi_0_t_plus
      self.pi_0_t_minus = pi_0_t_minus
      self.Out_sg_t = Out_sg_t
      self.In_sg_t = In_sg_t
      
    # ----------------- definition of setters -----------------
    def set_price_id(self, price_id):
        self.price_id = price_id
    
    def set_period_id(self, period_id):
        self.period_id = period_id
        
    def set_b0_t(self, b0_t):
        self.b0_t = b0_t
        
    def set_c0_t(self, c0_t):
        self.c0_t = c0_t
        
    def set_pi_0_t_plus(self, pi_0_t_plus):
        self.pi_0_t_plus = pi_0_t_plus
    
    def set_pi_0_t_minus(self, pi_0_t_minus):
        self.pi_0_t_minus = pi_0_t_minus
        
    def set_Out_sg_t(self, Out_sg_t):
        self.Out_sg_t = Out_sg_t
    
    def set_In_sg_t(self, In_sg_t):
        self.In_sg_t = In_sg_t
    
    # ----------------- definition of getters -----------------
    def get_price_id(self):
        return self.price_id
    
    def get_period_id(self):
        return self.period_id
        
    def get_b0_t(self):
        return self.b0_t
        
    def get_c0_t(self):
        return self.c0_t
        
    def get_pi_0_t_plus(self):
        return self.pi_0_t_plus
    
    def get_pi_0_t_minus(self):
        return self.pi_0_t_minus
        
    def get_Out_sg_t(self):
        return self.Out_sg_t
    
    def get_In_sg_t(self, In_sg_t):
        return self.In_sg_t
    