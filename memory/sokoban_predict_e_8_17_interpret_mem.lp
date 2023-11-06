% sokoban_predict_e_8_17
% Optimization:57

% Permanents

% Rules
rule_body(r1,isa2(p_below,var_c1,var_c2)).
rule_body(r1,s2(c_in_1,var_x,var_c2)).
rule_body(r1,s2(c_in_2,var_y,var_c1)).
rule_arrow_head(r1,s(c_p1,var_y)).

rule_body(r2,isa2(p_below,var_c1,var_c2)).
rule_body(r2,s2(c_in_1,var_x,var_c1)).
rule_body(r2,s2(c_in_2,var_y,var_c2)).
rule_arrow_head(r2,s(c_p1,var_y)).

rule_body(r3,isa2(p_right,var_c1,var_c2)).
rule_body(r3,s(c_east,var_x)).
rule_body(r3,s2(c_in_1,var_x,var_c1)).
rule_body(r3,s2(c_in_2,var_y,var_c2)).
rule_arrow_head(r3,s(c_p4,var_y)).

rule_body(r4,isa2(p_right,var_c2,var_c1)).
rule_body(r4,s2(c_in_1,var_x,var_c1)).
rule_body(r4,s2(c_in_2,var_y,var_c2)).
rule_arrow_head(r4,s(c_p4,var_y)).

rule_body(r10,isa2(p_below,var_c1,var_c2)).
rule_body(r10,s(c_p1,var_y)).
rule_body(r10,s(c_south,var_x)).
rule_body(r10,s2(c_in_2,var_y,var_c1)).
rule_head_causes(r10,s2(c_in_2,var_y,var_c2)).

rule_body(r11,isa2(p_below,var_c1,var_c2)).
rule_body(r11,s(c_north,var_x)).
rule_body(r11,s(c_p1,var_y)).
rule_body(r11,s2(c_in_2,var_y,var_c2)).
rule_head_causes(r11,s2(c_in_2,var_y,var_c1)).

rule_body(r12,isa2(p_right,var_c1,var_c2)).
rule_body(r12,s(c_east,var_x)).
rule_body(r12,s(c_p4,var_y)).
rule_body(r12,s2(c_in_2,var_y,var_c1)).
rule_head_causes(r12,s2(c_in_2,var_y,var_c2)).

rule_body(r5,isa2(p_below,var_c1,var_c2)).
rule_body(r5,s(c_south,var_x)).
rule_body(r5,s2(c_in_1,var_x,var_c1)).
rule_head_causes(r5,s2(c_in_1,var_x,var_c2)).

rule_body(r6,isa2(p_below,var_c1,var_c2)).
rule_body(r6,s(c_north,var_x)).
rule_body(r6,s2(c_in_1,var_x,var_c2)).
rule_head_causes(r6,s2(c_in_1,var_x,var_c1)).

rule_body(r7,isa(p_is_not_wall,var_c1)).
rule_body(r7,isa2(p_right,var_c2,var_c1)).
rule_body(r7,s(c_east,var_x)).
rule_body(r7,s2(c_in_1,var_x,var_c2)).
rule_head_causes(r7,s2(c_in_1,var_x,var_c1)).

rule_body(r8,isa2(p_right,var_c1,var_c2)).
rule_body(r8,s(c_west,var_x)).
rule_body(r8,s2(c_in_1,var_x,var_c2)).
rule_head_causes(r8,s2(c_in_1,var_x,var_c1)).

rule_body(r9,isa2(p_right,var_c2,var_c1)).
rule_body(r9,s(c_p4,var_y)).
rule_body(r9,s(c_west,var_x)).
rule_body(r9,s2(c_in_2,var_y,var_c1)).
rule_head_causes(r9,s2(c_in_2,var_y,var_c2)).


