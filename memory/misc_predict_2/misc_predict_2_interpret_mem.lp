% misc_predict_2
% Optimization:8

% Typing
is_type(t_cell).
is_type(t_grid).
is_type(t_object).
is_type(t_sensor_1).
is_type(t_sensor_2).
permanent(isa(t_cell,obj_sensor_a)).
permanent(isa(t_cell,obj_sensor_b)).
permanent(isa(t_grid,obj_grid)).
permanent(isa(t_object,obj_grid)).
permanent(isa(t_object,obj_sensor_a)).
permanent(isa(t_object,obj_sensor_b)).
permanent(isa(t_sensor_1,obj_sensor_a)).
permanent(isa(t_sensor_2,obj_sensor_b)).

% Concepts
is_concept(c_a).
is_concept(c_b).
is_concept(c_c).
is_concept(c_off).
is_concept(c_on).
is_concept(c_part).
is_concept(t_cell).
is_concept(t_grid).
is_concept(t_object).
is_concept(t_sensor_1).
is_concept(t_sensor_2).

% New permanents

% Given permanents

% Rules
rule_body(r1,s(c_on,var_sensor_1_1)).
rule_head_causes(r1,s(c_off,var_sensor_1_1)).

rule_body(r2,s(c_off,var_sensor_1_1)).
rule_head_causes(r2,s(c_on,var_sensor_1_1)).



