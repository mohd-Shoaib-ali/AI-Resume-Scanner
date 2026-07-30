import ResumeUpload from "./components/ResumeUpload";
import ResumeList from "./components/ResumeList";
import JobForm from "./components/JobForm";
import JobList from "./components/JobList";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="max-w-4xl mx-auto py-8">
        <h1 className="text-2xl font-bold mb-4">
          AI Resume Screening Platform
        </h1>

        <div className="grid md:grid-cols-2 gap-4">
          <div>
            <ResumeUpload />
            <ResumeList />
          </div>
          <div>
            <JobForm />
            <JobList />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
