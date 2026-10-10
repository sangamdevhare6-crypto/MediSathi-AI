document.addEventListener("DOMContentLoaded",()=>{
  const toggle=document.getElementById("menuToggle"), sidebar=document.getElementById("sidebar");
  if(toggle&&sidebar) toggle.addEventListener("click",()=>sidebar.classList.toggle("sidebar-open"));
  const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in-view");observer.unobserve(e.target)}}),{threshold:.08});
  document.querySelectorAll(".stat-card,.quick-card,.panel,.hero-banner,.safety-banner").forEach(el=>{el.classList.add("reveal");observer.observe(el)});
  document.querySelectorAll("input,textarea,select").forEach(el=>{el.classList.add("form-control")});
  document.querySelectorAll(".toast").forEach(el=>{setTimeout(()=>{el.classList.add("toast-hide")},4500)});
});