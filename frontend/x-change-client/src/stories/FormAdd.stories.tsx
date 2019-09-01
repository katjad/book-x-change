import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import { FormAdd } from "../components/moleculesIndex";

storiesOf("Forms", module)
  .add("Form to add book", () => <FormAdd />)
