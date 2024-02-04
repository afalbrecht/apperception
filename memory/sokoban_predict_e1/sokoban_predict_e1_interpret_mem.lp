% sokoban_predict_e1
% Optimization:84

% Typing
is_type(t_block).
is_type(t_cell).
is_type(t_object).
is_type(t_player).
permanent(isa(t_block,obj_x2)).
permanent(isa(t_block,obj_x3)).
permanent(isa(t_block,obj_x4)).
permanent(isa(t_cell,obj_cell_1_1)).
permanent(isa(t_cell,obj_cell_1_2)).
permanent(isa(t_cell,obj_cell_1_3)).
permanent(isa(t_cell,obj_cell_1_4)).
permanent(isa(t_cell,obj_cell_2_1)).
permanent(isa(t_cell,obj_cell_2_2)).
permanent(isa(t_cell,obj_cell_2_3)).
permanent(isa(t_cell,obj_cell_2_4)).
permanent(isa(t_cell,obj_cell_3_1)).
permanent(isa(t_cell,obj_cell_3_2)).
permanent(isa(t_cell,obj_cell_3_3)).
permanent(isa(t_cell,obj_cell_3_4)).
permanent(isa(t_cell,obj_cell_4_1)).
permanent(isa(t_cell,obj_cell_4_2)).
permanent(isa(t_cell,obj_cell_4_3)).
permanent(isa(t_cell,obj_cell_4_4)).
permanent(isa(t_cell,obj_cell_5_1)).
permanent(isa(t_cell,obj_cell_5_2)).
permanent(isa(t_cell,obj_cell_5_3)).
permanent(isa(t_cell,obj_cell_5_4)).
permanent(isa(t_object,obj_cell_1_1)).
permanent(isa(t_object,obj_cell_1_2)).
permanent(isa(t_object,obj_cell_1_3)).
permanent(isa(t_object,obj_cell_1_4)).
permanent(isa(t_object,obj_cell_2_1)).
permanent(isa(t_object,obj_cell_2_2)).
permanent(isa(t_object,obj_cell_2_3)).
permanent(isa(t_object,obj_cell_2_4)).
permanent(isa(t_object,obj_cell_3_1)).
permanent(isa(t_object,obj_cell_3_2)).
permanent(isa(t_object,obj_cell_3_3)).
permanent(isa(t_object,obj_cell_3_4)).
permanent(isa(t_object,obj_cell_4_1)).
permanent(isa(t_object,obj_cell_4_2)).
permanent(isa(t_object,obj_cell_4_3)).
permanent(isa(t_object,obj_cell_4_4)).
permanent(isa(t_object,obj_cell_5_1)).
permanent(isa(t_object,obj_cell_5_2)).
permanent(isa(t_object,obj_cell_5_3)).
permanent(isa(t_object,obj_cell_5_4)).
permanent(isa(t_object,obj_x1)).
permanent(isa(t_object,obj_x2)).
permanent(isa(t_object,obj_x3)).
permanent(isa(t_object,obj_x4)).
permanent(isa(t_player,obj_x1)).

% Concepts
is_concept(c_east).
is_concept(c_in_1).
is_concept(c_in_2).
is_concept(c_noop).
is_concept(c_north).
is_concept(c_p1).
is_concept(c_p2).
is_concept(c_p3).
is_concept(c_p4).
is_concept(c_south).
is_concept(c_west).
is_concept(east).
is_concept(in_1).
is_concept(in_2).
is_concept(noop).
is_concept(north).
is_concept(p_below).
is_concept(p_is_not_wall).
is_concept(p_is_wall).
is_concept(p_right).
is_concept(south).
is_concept(t_block).
is_concept(t_cell).
is_concept(t_object).
is_concept(t_player).
is_concept(west).

% New permanents

% Given permanents
permanent(isa(p_is_not_wall,obj_cell_1_1)).
permanent(isa(p_is_not_wall,obj_cell_1_2)).
permanent(isa(p_is_not_wall,obj_cell_1_3)).
permanent(isa(p_is_not_wall,obj_cell_1_4)).
permanent(isa(p_is_not_wall,obj_cell_2_1)).
permanent(isa(p_is_not_wall,obj_cell_2_2)).
permanent(isa(p_is_not_wall,obj_cell_2_3)).
permanent(isa(p_is_not_wall,obj_cell_2_4)).
permanent(isa(p_is_not_wall,obj_cell_3_1)).
permanent(isa(p_is_not_wall,obj_cell_3_2)).
permanent(isa(p_is_not_wall,obj_cell_3_3)).
permanent(isa(p_is_not_wall,obj_cell_3_4)).
permanent(isa(p_is_not_wall,obj_cell_4_1)).
permanent(isa(p_is_not_wall,obj_cell_4_2)).
permanent(isa(p_is_not_wall,obj_cell_4_3)).
permanent(isa(p_is_not_wall,obj_cell_4_4)).
permanent(isa(p_is_not_wall,obj_cell_5_1)).
permanent(isa(p_is_not_wall,obj_cell_5_2)).
permanent(isa(p_is_not_wall,obj_cell_5_3)).
permanent(isa(p_is_not_wall,obj_cell_5_4)).
permanent(isa2(p_below,obj_cell_1_1,obj_cell_1_2)).
permanent(isa2(p_below,obj_cell_1_2,obj_cell_1_3)).
permanent(isa2(p_below,obj_cell_1_3,obj_cell_1_4)).
permanent(isa2(p_below,obj_cell_2_1,obj_cell_2_2)).
permanent(isa2(p_below,obj_cell_2_2,obj_cell_2_3)).
permanent(isa2(p_below,obj_cell_2_3,obj_cell_2_4)).
permanent(isa2(p_below,obj_cell_3_1,obj_cell_3_2)).
permanent(isa2(p_below,obj_cell_3_2,obj_cell_3_3)).
permanent(isa2(p_below,obj_cell_3_3,obj_cell_3_4)).
permanent(isa2(p_below,obj_cell_4_1,obj_cell_4_2)).
permanent(isa2(p_below,obj_cell_4_2,obj_cell_4_3)).
permanent(isa2(p_below,obj_cell_4_3,obj_cell_4_4)).
permanent(isa2(p_below,obj_cell_5_1,obj_cell_5_2)).
permanent(isa2(p_below,obj_cell_5_2,obj_cell_5_3)).
permanent(isa2(p_below,obj_cell_5_3,obj_cell_5_4)).
permanent(isa2(p_right,obj_cell_1_1,obj_cell_2_1)).
permanent(isa2(p_right,obj_cell_1_2,obj_cell_2_2)).
permanent(isa2(p_right,obj_cell_1_3,obj_cell_2_3)).
permanent(isa2(p_right,obj_cell_1_4,obj_cell_2_4)).
permanent(isa2(p_right,obj_cell_2_1,obj_cell_3_1)).
permanent(isa2(p_right,obj_cell_2_2,obj_cell_3_2)).
permanent(isa2(p_right,obj_cell_2_3,obj_cell_3_3)).
permanent(isa2(p_right,obj_cell_2_4,obj_cell_3_4)).
permanent(isa2(p_right,obj_cell_3_1,obj_cell_4_1)).
permanent(isa2(p_right,obj_cell_3_2,obj_cell_4_2)).
permanent(isa2(p_right,obj_cell_3_3,obj_cell_4_3)).
permanent(isa2(p_right,obj_cell_3_4,obj_cell_4_4)).
permanent(isa2(p_right,obj_cell_4_1,obj_cell_5_1)).
permanent(isa2(p_right,obj_cell_4_2,obj_cell_5_2)).
permanent(isa2(p_right,obj_cell_4_3,obj_cell_5_3)).
permanent(isa2(p_right,obj_cell_4_4,obj_cell_5_4)).

% Rules
rule_body(r1,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r1,s2(c_in_1,var_player_1,var_cell_2)).
rule_body(r1,s2(c_in_2,var_block_1,var_cell_1)).
rule_arrow_head(r1,s(c_p1,var_block_1)).

rule_body(r2,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r2,s2(c_in_1,var_player_1,var_cell_1)).
rule_body(r2,s2(c_in_2,var_block_1,var_cell_2)).
rule_arrow_head(r2,s(c_p1,var_block_1)).

rule_body(r3,isa2(p_right,var_cell_1,var_cell_2)).
rule_body(r3,s(c_east,var_player_1)).
rule_body(r3,s2(c_in_1,var_player_1,var_cell_1)).
rule_body(r3,s2(c_in_2,var_block_1,var_cell_2)).
rule_arrow_head(r3,s(c_p4,var_block_1)).

rule_body(r4,isa2(p_right,var_cell_2,var_cell_1)).
rule_body(r4,s2(c_in_1,var_player_1,var_cell_1)).
rule_body(r4,s2(c_in_2,var_block_1,var_cell_2)).
rule_arrow_head(r4,s(c_p4,var_block_1)).

rule_body(r10,isa2(p_right,var_cell_1,var_cell_2)).
rule_body(r10,s(c_east,var_player_1)).
rule_body(r10,s(c_p4,var_block_1)).
rule_body(r10,s2(c_in_2,var_block_1,var_cell_1)).
rule_head_causes(r10,s2(c_in_2,var_block_1,var_cell_2)).

rule_body(r11,isa2(p_right,var_cell_2,var_cell_1)).
rule_body(r11,s(c_p4,var_block_1)).
rule_body(r11,s(c_west,var_player_1)).
rule_body(r11,s2(c_in_2,var_block_1,var_cell_1)).
rule_head_causes(r11,s2(c_in_2,var_block_1,var_cell_2)).

rule_body(r12,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r12,s(c_north,var_player_1)).
rule_body(r12,s(c_p1,var_block_1)).
rule_body(r12,s2(c_in_2,var_block_1,var_cell_2)).
rule_head_causes(r12,s2(c_in_2,var_block_1,var_cell_1)).

rule_body(r5,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r5,s(c_south,var_player_1)).
rule_body(r5,s2(c_in_1,var_player_1,var_cell_1)).
rule_head_causes(r5,s2(c_in_1,var_player_1,var_cell_2)).

rule_body(r6,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r6,s(c_north,var_player_1)).
rule_body(r6,s2(c_in_1,var_player_1,var_cell_2)).
rule_head_causes(r6,s2(c_in_1,var_player_1,var_cell_1)).

rule_body(r7,isa(p_is_not_wall,var_cell_1)).
rule_body(r7,isa2(p_right,var_cell_2,var_cell_1)).
rule_body(r7,s(c_east,var_player_1)).
rule_body(r7,s2(c_in_1,var_player_1,var_cell_2)).
rule_head_causes(r7,s2(c_in_1,var_player_1,var_cell_1)).

rule_body(r8,isa2(p_right,var_cell_1,var_cell_2)).
rule_body(r8,s(c_west,var_player_1)).
rule_body(r8,s2(c_in_1,var_player_1,var_cell_2)).
rule_head_causes(r8,s2(c_in_1,var_player_1,var_cell_1)).

rule_body(r9,isa2(p_below,var_cell_1,var_cell_2)).
rule_body(r9,s(c_p1,var_block_1)).
rule_body(r9,s(c_south,var_player_1)).
rule_body(r9,s2(c_in_2,var_block_1,var_cell_1)).
rule_head_causes(r9,s2(c_in_2,var_block_1,var_cell_2)).



