COPY
(select cs_tdf_gc.name, cs_tdf_gc.team, cs_tdf_gc.points as TDF_GC,
	CASE WHEN cs_tdf_mountains.points IS NULL 
		THEN 0
		ELSE cs_tdf_mountains.points END TDF_Mountains,
	CASE WHEN cs_tdf_points.points IS NULL 
		THEN 0
		ELSE cs_tdf_points.points END TDF_Points,
	CASE WHEN cs_individual_americatour.points IS NULL 
		THEN 0
		ELSE cs_individual_americatour.points END AMERICA_TOUR,
	CASE WHEN cs_individual_europetour.points IS NULL 
		THEN 0
		ELSE cs_individual_europetour.points END EUROPE_TOUR,
	CASE WHEN cs_individual_gc.points IS NULL 
		THEN 0
		ELSE cs_individual_gc.points END GC,
	CASE WHEN cs_individual_hills.points IS NULL 
		THEN 0
		ELSE cs_individual_hills.points END HILLS,
	CASE WHEN cs_individual_mountains.points IS NULL 
		THEN 0
		ELSE cs_individual_mountains.points END MOUNTAINS,
	CASE WHEN cs_individual_oneday.points IS NULL 
		THEN 0
		ELSE cs_individual_oneday.points END ONEDAY,
	CASE WHEN cs_individual_pcs_rank.points IS NULL 
		THEN 0
		ELSE cs_individual_pcs_rank.points END PCS_RANK,
	CASE WHEN cs_individual_prologue.points IS NULL 
		THEN 0
		ELSE cs_individual_prologue.points END PROLOGUE,
	CASE WHEN cs_individual_sprint.points IS NULL 
		THEN 0
		ELSE cs_individual_sprint.points END SPRINT,
	CASE WHEN cs_individual_worldtour.points IS NULL 
		THEN 0
		ELSE cs_individual_worldtour.points END WORLD_TOUR
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
)
TO '/tmp/stats.csv' DELIMITER ',' CSV HEADER;