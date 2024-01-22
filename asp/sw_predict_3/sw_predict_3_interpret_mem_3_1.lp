% sw_predict_3

% Permanents
permanent(isa2(p_succ,obj_letter_b,obj_letter_a)).
permanent(isa2(p_succ,obj_letter_c,obj_letter_b)).
permanent(isa2(p_succ,obj_letter_a,obj_letter_d)).
permanent(isa2(p_succ,obj_letter_d,obj_letter_c)).
permanent(isa2(p_succ,obj_letter_e,obj_letter_d)).
permanent(isa(p_p2,obj_gen_1)).
permanent(isa2(p_r,obj_gen_1,obj_gen_2)).
permanent(isa(p_p1,obj_gen_2)).
permanent(isa2(p_r,obj_gen_2,obj_gen_2)).
permanent(isa(p_p1,obj_gen_3)).
permanent(isa2(p_r,obj_gen_3,obj_gen_3)).

% Rules
rule_body(r1,isa2(p_succ,var_letter_1,var_letter_2)).
rule_body(r1,s2(c_letter,var_sensor_1,var_letter_2)).
rule_head_causes(r1,s2(c_letter,var_sensor_1,var_letter_1)).

