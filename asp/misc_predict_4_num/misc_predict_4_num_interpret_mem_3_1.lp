% misc_predict_4_num

% Permanents
permanent(isa2(p_part,obj_sensor,obj_grid)).
permanent(isa2(p_succ,obj_number_0,obj_number_8)).
permanent(isa2(p_succ,obj_number_1,obj_number_0)).
permanent(isa2(p_succ,obj_number_2,obj_number_1)).
permanent(isa2(p_succ,obj_number_3,obj_number_2)).
permanent(isa2(p_succ,obj_number_4,obj_number_3)).
permanent(isa2(p_succ,obj_number_5,obj_number_4)).
permanent(isa2(p_succ,obj_number_6,obj_number_5)).
permanent(isa2(p_succ,obj_number_7,obj_number_6)).
permanent(isa2(p_succ,obj_number_8,obj_number_7)).

% Rules
rule_body(r1,isa2(p_succ,var_number_1,var_number_2)).
rule_body(r1,s2(c_number,var_sensor_1,var_number_2)).
rule_head_causes(r1,s2(c_number,var_sensor_1,var_number_1)).

