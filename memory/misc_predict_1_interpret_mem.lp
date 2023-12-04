% misc_predict_1
% Optimization:7

% Typing
is_type(t_object).
is_type(t_sensor).
permanent(isa(t_object,obj_sensor_a)).

% Concepts
is_concept(c_off).
is_concept(c_on).
is_concept(t_object).
is_concept(t_sensor).

% New permanents

% Given permanents

% Rules
rule_body(r1,s(c_on,var_x)).
rule_head_causes(r1,s(c_off,var_x)).

rule_body(r2,s(c_off,var_x)).
rule_head_causes(r2,s(c_on,var_x)).

rule_body(r3,s(c_on,var_x)).
rule_head_causes(r3,s(c_off,var_x)).



