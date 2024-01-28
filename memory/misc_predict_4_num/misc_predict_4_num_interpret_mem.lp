% misc_predict_4_num
% Optimization:9

% Typing
is_type(t_number).
is_type(t_object).
is_type(t_sensor).
permanent(isa(t_number,obj_number_0)).
permanent(isa(t_number,obj_number_1)).
permanent(isa(t_number,obj_number_2)).
permanent(isa(t_number,obj_number_3)).
permanent(isa(t_number,obj_number_4)).
permanent(isa(t_number,obj_number_5)).
permanent(isa(t_number,obj_number_6)).
permanent(isa(t_number,obj_number_7)).
permanent(isa(t_number,obj_number_8)).
permanent(isa(t_object,obj_sensor)).
permanent(isa(t_sensor,obj_sensor)).

% Concepts
is_concept(c_number).
is_concept(p_succ).
is_concept(t_number).
is_concept(t_object).
is_concept(t_sensor).

% New permanents

% Given permanents
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



