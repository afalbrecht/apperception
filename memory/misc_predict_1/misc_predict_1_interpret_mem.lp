% misc_predict_1
% Optimization:9

% Typing
is_type(t_object).
is_type(t_sensor_1).
permanent(isa(t_object,obj_sensor_a)).
permanent(isa(t_sensor_1,obj_sensor_a)).

% Concepts
is_concept(c_off).
is_concept(c_on).
is_concept(t_object).
is_concept(t_sensor_1).

% New permanents

% Given permanents

% Rules
rule_body(r1,s(c_on,var_sensor_1_1)).
rule_head_causes(r1,s(c_off,var_sensor_1_1)).

rule_body(r2,s(c_off,var_sensor_1_1)).
rule_head_causes(r2,s(c_on,var_sensor_1_1)).



