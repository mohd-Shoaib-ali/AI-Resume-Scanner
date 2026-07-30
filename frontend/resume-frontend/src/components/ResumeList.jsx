import { useEffect, useState } from "react";
import api from "../api/client";

export default function ResumeList() {
  const [resumes, setResumes] = useState([]);

  useEffect(() => {
    const fetchResumes = async () => {
      try {
        const res = await api.get("/resume/");
        setResumes(res.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchResumes();
  }, []);

  return (
    <div className="p-4 border rounded">
      <h2 className="text-lg font-semibold mb-2">Resumes</h2>
      <ul className="space-y-2 text-sm">
        {resumes.map((r) => (
          <li key={r.id} className="border-b pb-2">
            <div><strong>{r.name || "(no name)"}</strong></div>
            <div>{r.email}</div>
            <div className="text-gray-600 text-xs">{r.file_name}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}