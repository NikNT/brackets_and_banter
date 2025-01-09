import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { wishListSchema } from "../schemas/wishListSchema";
import axios from "axios";

const Form = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(wishListSchema),
    defaultValues: {
      name: "",
      description: "",
      priority: "Medium",
    },
  });
  const onSubmit = (data) => {
    axios
      .post("http://localhost:8000/api/wishlist/", data)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    console.log("Handle Submit", data);
  };

  return (
    <>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Name:</label>
          <input {...register("name")} />
          {errors.name && <span>{errors.name.message}</span>}
        </div>

        <div>
          <label>Description</label>
          <textarea {...register("description")} />
        </div>

        <div>
          <label>Priority</label>
          <select {...register("priority")}>
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>

        <button type="submit">Submit</button>
      </form>
    </>
  );
};

export default Form;
