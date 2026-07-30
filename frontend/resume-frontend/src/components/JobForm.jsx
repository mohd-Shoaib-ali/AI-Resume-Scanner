import { useState } from "react";
import api from "../api/client";

export default function JobForm({ onCreated }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [skills, setSkills] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/jobs/", {
        title,
        description,
        skills,
      });
      onCreated && onCreated(res.data);
      setTitle("");
      setDescription("");
      setSkills("");
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="p-4 border rounded mb-4">
      <h2 className="text-lg font-semibold mb-2">Create Job</h2>
      <form onSubmit={handleSubmit} className="space-y-2">
        <input
          className="w-full border px-2 py-1"
          placeholder="Job Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          className="w-full border px-2 py-1"
          rows={4}
          placeholder="Job Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <input
          className="w-full border px-2 py-1"
          placeholder="Skills (comma-separated)"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
        />
        <button
          type="submit"
          className="px-4 py-2 bg-green-600 text-white rounded"
        >
          Save Job
        </button>
      </form>
    </div>
  );
}