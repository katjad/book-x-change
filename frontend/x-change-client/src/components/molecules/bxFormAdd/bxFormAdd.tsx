import * as React from "react";
import { Formik, FieldProps, FormikProps, Field, ErrorMessage } from "formik";
import * as Yup from 'yup';
import { Form, Container, Header, Button } from 'semantic-ui-react';

/**** Book fields ****
ISBN
Title    x
Author
Description
Year published
Category x
At Framework x
******/


interface IFormValues {
  title: string,
  category: string,
  at_framework: boolean
}

const initialValues: IFormValues = {
  title: "",
  category: "programming",
  at_framework: false
}


const BxForm = () => {
  return (
    <Container>
      <Container className="push-down" text>
        <Header as="h2">Add a Book</Header>
      </Container>
      <Formik
        initialValues={initialValues}
        onSubmit={(values: IFormValues, { setSubmitting }) => {
          setTimeout(() => {
            alert(JSON.stringify(values, null, 2));
            setSubmitting(false);
          }, 400);
        }}
        validationSchema={Yup.object().shape({
            title: Yup.string().required("Please enter a title.")
        })}
      >
        {( props: FormikProps<unknown> ) => (
            <Form onSubmit={props.handleSubmit}>
              <Container className="push-down" text>
                <Field
                  name="title"
                  type="text"
                  placeholder="Title"
                />
                <ErrorMessage component="div" className="alert-error" name="title" />
              </Container>

              <Container className="push-down" text>
                <Field
                  name="category"
                  component="select"
                >
                  <option value="programming">Programming</option>
                  <option value="design">Design &amp; UX</option>
                  <option value="tech">Technology</option>
                  <option value="science">Science</option>
                  <option value="psychology">Psychology</option>
                </Field>
              </Container>

              <Container className="push-down" text>
                <Field
                  name="at_framework"
                  render={( props: FieldProps<unknown> )  => {
                    return (
                      <div className="flex-container">
                        <input className="flex-checkbox" type="checkbox" {...props.field} />
                        <label htmlFor="at_framework">
                          At Framework?
                        </label>
                      </div>
                    )}}
                />
              </Container>

              <Container text>
              <Button type="submit">Add book</Button>
              </Container>
            </Form>
            )}

      </Formik>
    </Container>
  )
}

export default BxForm
