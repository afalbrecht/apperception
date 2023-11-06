% misc_predict_4_num
% Optimization:4

% Typing
is_type(t_grid).
is_type(t_number).
is_type(t_object).
is_type(t_sensor).
permanent(isa(t_grid,obj_grid)).
permanent(isa(t_number,obj_number_0)).
permanent(isa(t_number,obj_number_1)).
permanent(isa(t_number,obj_number_2)).
permanent(isa(t_number,obj_number_3)).
permanent(isa(t_number,obj_number_4)).
permanent(isa(t_number,obj_number_5)).
permanent(isa(t_number,obj_number_6)).
permanent(isa(t_number,obj_number_7)).
permanent(isa(t_number,obj_number_8)).
permanent(isa(t_number,obj_number_9)).
permanent(isa(t_object,obj_sensor)).
permanent(isa(t_sensor,obj_sensor)).

% Concepts
is_concept(c_number).
is_concept(p_first_number).
is_concept(p_less).
is_concept(p_part).
is_concept(p_succ).
is_concept(t_grid).
is_concept(t_number).
is_concept(t_object).
is_concept(t_sensor).

% New permanents

% Given permanents
permanent(isa(p_first_number,obj_number_0)).
permanent(isa2(p_less,obj_number_0,obj_number_1)).
permanent(isa2(p_less,obj_number_0,obj_number_2)).
permanent(isa2(p_less,obj_number_0,obj_number_3)).
permanent(isa2(p_less,obj_number_0,obj_number_4)).
permanent(isa2(p_less,obj_number_0,obj_number_5)).
permanent(isa2(p_less,obj_number_0,obj_number_6)).
permanent(isa2(p_less,obj_number_0,obj_number_7)).
permanent(isa2(p_less,obj_number_0,obj_number_8)).
permanent(isa2(p_less,obj_number_0,obj_number_9)).
permanent(isa2(p_less,obj_number_1,obj_number_2)).
permanent(isa2(p_less,obj_number_1,obj_number_3)).
permanent(isa2(p_less,obj_number_1,obj_number_4)).
permanent(isa2(p_less,obj_number_1,obj_number_5)).
permanent(isa2(p_less,obj_number_1,obj_number_6)).
permanent(isa2(p_less,obj_number_1,obj_number_7)).
permanent(isa2(p_less,obj_number_1,obj_number_8)).
permanent(isa2(p_less,obj_number_1,obj_number_9)).
permanent(isa2(p_less,obj_number_2,obj_number_3)).
permanent(isa2(p_less,obj_number_2,obj_number_4)).
permanent(isa2(p_less,obj_number_2,obj_number_5)).
permanent(isa2(p_less,obj_number_2,obj_number_6)).
permanent(isa2(p_less,obj_number_2,obj_number_7)).
permanent(isa2(p_less,obj_number_2,obj_number_8)).
permanent(isa2(p_less,obj_number_2,obj_number_9)).
permanent(isa2(p_less,obj_number_3,obj_number_4)).
permanent(isa2(p_less,obj_number_3,obj_number_5)).
permanent(isa2(p_less,obj_number_3,obj_number_6)).
permanent(isa2(p_less,obj_number_3,obj_number_7)).
permanent(isa2(p_less,obj_number_3,obj_number_8)).
permanent(isa2(p_less,obj_number_3,obj_number_9)).
permanent(isa2(p_less,obj_number_4,obj_number_5)).
permanent(isa2(p_less,obj_number_4,obj_number_6)).
permanent(isa2(p_less,obj_number_4,obj_number_7)).
permanent(isa2(p_less,obj_number_4,obj_number_8)).
permanent(isa2(p_less,obj_number_4,obj_number_9)).
permanent(isa2(p_less,obj_number_5,obj_number_6)).
permanent(isa2(p_less,obj_number_5,obj_number_7)).
permanent(isa2(p_less,obj_number_5,obj_number_8)).
permanent(isa2(p_less,obj_number_5,obj_number_9)).
permanent(isa2(p_less,obj_number_6,obj_number_7)).
permanent(isa2(p_less,obj_number_6,obj_number_8)).
permanent(isa2(p_less,obj_number_6,obj_number_9)).
permanent(isa2(p_less,obj_number_7,obj_number_8)).
permanent(isa2(p_less,obj_number_7,obj_number_9)).
permanent(isa2(p_less,obj_number_8,obj_number_8)).
permanent(isa2(p_less,obj_number_8,obj_number_9)).
permanent(isa2(p_less,obj_number_9,obj_number_8)).
permanent(isa2(p_less,obj_number_9,obj_number_9)).
permanent(isa2(p_part,obj_sensor,obj_grid)).
permanent(isa2(p_succ,obj_number_0,obj_number_1)).
permanent(isa2(p_succ,obj_number_1,obj_number_2)).
permanent(isa2(p_succ,obj_number_2,obj_number_3)).
permanent(isa2(p_succ,obj_number_3,obj_number_4)).
permanent(isa2(p_succ,obj_number_4,obj_number_5)).
permanent(isa2(p_succ,obj_number_5,obj_number_6)).
permanent(isa2(p_succ,obj_number_6,obj_number_7)).
permanent(isa2(p_succ,obj_number_7,obj_number_8)).
permanent(isa2(p_succ,obj_number_8,obj_number_9)).
permanent(isa2(p_succ,obj_number_9,obj_number_8)).

% Rules
rule_body(r1,isa2(p_succ,var_l,var_l2)).
rule_body(r1,s2(c_number,var_s,var_l)).
rule_head_causes(r1,s2(c_number,var_s,var_l2)).


