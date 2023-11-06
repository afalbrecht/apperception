% misc_first_last_1
% Optimization:15 8

% Permanents

% Rules
rule_body(r1,isa2(p_right,var_x,var_y)).
rule_body(r1,s(c_off,var_x)).
rule_head_causes(r1,s(c_off,var_y)).

rule_body(r2,s(c_off,var_x)).
rule_head_causes(r2,s(c_on,var_x)).


