% misc_predict_4

% Permanents
permanent(isa2(p_part,obj_sensor,obj_grid)).
permanent(isa2(p_succ,obj_letter_a,obj_letter_f)).
permanent(isa2(p_succ,obj_letter_b,obj_letter_a)).
permanent(isa2(p_succ,obj_letter_c,obj_letter_b)).
permanent(isa2(p_succ,obj_letter_d,obj_letter_c)).
permanent(isa2(p_succ,obj_letter_e,obj_letter_d)).
permanent(isa2(p_succ,obj_letter_f,obj_letter_e)).

% Rules
rule_body(r1,isa2(p_succ,var_letter_1,var_letter_2)).
rule_body(r1,s2(c_letter,var_sensor_1,var_letter_2)).
rule_head_causes(r1,s2(c_letter,var_sensor_1,var_letter_1)).

