select cs_tdf_gc.name,cs_tdf_gc.points as TDF_GC,cs_tdf_mountains.points as TDF_Mountain ,cs_tdf_points.points as TDF_Points,
	cs_individual_americatour.points as AMERICA_TOUR, cs_individual_europetour.points as EUROPE_TOUR, cs_individual_gc.points as GC,
	cs_individual_hills.points as HILLS, cs_individual_mountains.points as MOUNTAINS, cs_individual_oneday.points as ONEDAY, 
	cs_individual_pcs_rank.points as PCS_RANK, cs_individual_prologue.points as PROLOGUE, cs_individual_sprint.points as SPRINT,
	cs_individual_worldtour.points as WORLD_TOUR
from cs_tdf_gc left outer join cs_tdf_mountains on cs_tdf_gc.name = cs_tdf_mountains.name 
	left outer join cs_tdf_points on cs_tdf_gc.name = cs_tdf_points.name
	left outer join cs_individual_americatour on ((cs_tdf_gc.name = cs_individual_americatour.name) AND extract(year from cs_individual_americatour.timestamp) = 2013)
	left outer join cs_individual_europetour on ((cs_tdf_gc.name = cs_individual_europetour.name) AND extract(year from cs_individual_europetour.timestamp) = 2013)
	left outer join cs_individual_gc on ((cs_tdf_gc.name = cs_individual_gc.name) AND extract(year from cs_individual_gc.timestamp) = 2013)
	left outer join cs_individual_hills on ((cs_tdf_gc.name = cs_individual_hills.name) AND extract(year from cs_individual_hills.timestamp) = 2013)
	left outer join cs_individual_mountains on ((cs_tdf_gc.name = cs_individual_mountains.name) AND extract(year from cs_individual_mountains.timestamp) = 2013)
	left outer join cs_individual_oneday on ((cs_tdf_gc.name = cs_individual_oneday.name) AND extract(year from cs_individual_oneday.timestamp) = 2013)
	left outer join cs_individual_pcs_rank on ((cs_tdf_gc.name = cs_individual_pcs_rank.name) AND extract(year from cs_individual_pcs_rank.timestamp) = 2013)
	left outer join cs_individual_prologue on ((cs_tdf_gc.name = cs_individual_prologue.name) AND extract(year from cs_individual_prologue.timestamp) = 2013)
	left outer join cs_individual_sprint on ((cs_tdf_gc.name = cs_individual_sprint.name) AND extract(year from cs_individual_sprint.timestamp) = 2013)
	left outer join cs_individual_worldtour on ((cs_tdf_gc.name = cs_individual_worldtour.name) AND extract(year from cs_individual_worldtour.timestamp) = 2013) 
