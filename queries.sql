--1
select date_trunc('hour', time), count(*) from
public.mangement_advertiser_abstractclickviews
group by date_trunc('hour', time) order by date_trunc('hour', time)


--2
select
cast ((SELECT count(*) FROM public.mangement_advertiser_click join public.mangement_advertiser_abstractclickviews on id = abstractclickviews_ptr_id) as float) 
/
cast((SELECT count(*) FROM public.mangement_advertiser_view join public.mangement_advertiser_abstractclickviews on id = abstractclickviews_ptr_id) as float)
as ratio;

select time, c.countclick,k.countview, CAST(c.countclick AS float)/CAST(k.countview AS float) as ratio from
(Select date_trunc('hour', a.time) as time ,count(*) as countClick from
(SELECT * FROM public.mangement_advertiser_click join public.mangement_advertiser_abstractclickviews on id = abstractclickviews_ptr_id) as a 
group by date_trunc('hour', a.time) order by date_trunc('hour', a.time)) as c
natural join
(Select date_trunc('hour', b.time) as time ,count(*) as countView from
(SELECT * FROM public.mangement_advertiser_view join public.mangement_advertiser_abstractclickviews on id = abstractclickviews_ptr_id) as b
group by date_trunc('hour', b.time) order by date_trunc('hour', b.time)) as k  order by time desc;

--3