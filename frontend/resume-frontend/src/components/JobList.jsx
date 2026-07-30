import { useEffect, useState } from "react";
import api from "../api/client";

export default function JobList() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const res = await api.get("/jobs/");
        setJobs(res.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchJobs();
  }, []);

  return (
    <div className="p-4 border rounded">
      <h2 className="text-lg font-semibold mb-2">Jobs</h2>
      <ul className="space-y-2 text-sm">
        {jobs.map((j) => (
          <li key={j.id} className="border-b pb-2">
            <div><strong>{j.title}</strong></div>
            <div className="text-xs text-gray-700">{j.skills}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}