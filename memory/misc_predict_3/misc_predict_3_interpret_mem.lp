% misc_predict_3
% Optimization:15

% Typing
is_type(t_object).
is_type(t_sensor_2).
permanent(isa(t_object,obj_sensor_a)).
permanent(isa(t_sensor_2,obj_sensor_a)).

% Concepts
is_concept(c_a).
is_concept(c_b).
is_concept(c_c).
is_concept(c_d).
is_concept(t_object).
is_concept(t_sensor_2).

% New permanents

% Given permanents

% Rules
rule_body(r1,s(c_a,var_sensor_2_1)).
rule_head_causes(r1,s(c_b,var_sensor_2_1)).

rule_body(r2,s(c_d,var_sensor_2_1)).
rule_head_causes(r2,s(c_a,var_sensor_2_1)).

rule_body(r3,s(c_b,var_sensor_2_1)).
rule_head_causes(r3,s(c_c,var_sensor_2_1)).

rule_body(r4,s(c_c,var_sensor_2_1)).
rule_head_causes(r4,s(c_d,var_sensor_2_1)).



